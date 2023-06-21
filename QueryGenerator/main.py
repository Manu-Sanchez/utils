import json

from functools import reduce
from operator import iand, ior

from boto3.dynamodb.conditions import Attr

def generate_query(query):
  """
  Generates a query from a dict
  For dynamoDB queries the available conditions are AND and OR
  other conditions can be implemented
  
  :param query: dict
  :param query: It's a dictionary that contains all the keys
  :rtype: tuple(str, boto3.dynamodb.conditions)
  :return Query in str format and for dynamodb
  """
  expressions = [(0, query)]
  nodes = []

  for father_idx, expression in expressions:
      for operator, conditions in expression.items():

          if len(conditions) < 2: raise NotImplementedError
          elif type(conditions) != list: raise NotImplementedError

          node_idx = len(nodes)
          nodes.append({
              "operator": operator,
              "conditions": [],
              "dynamo_conditions": [],
              "node_idx": node_idx,
              "father_idx": father_idx
          })
          for condition in conditions:
              for key, value in condition.items():
                  if type(value) == list:
                      expressions.append((node_idx, condition))
                  else:
                      nodes[node_idx]["conditions"].append(f"{key}={value}")
                      nodes[node_idx]["dynamo_conditions"].append(Attr(key).eq(value))

  while nodes:
      node = nodes.pop()
      operator = node["operator"]
      conditions = node["conditions"]
      dynamo_conditions = node["dynamo_conditions"]
      father_idx = node["father_idx"]
      node_idx = node["node_idx"]

      str_conditions = f" {operator} ".join(conditions)

      if operator == "AND":
          operator = iand
      else:
          operator = ior

      if node_idx == 0:
          print(str_conditions)
          print(reduce(operator, dynamo_conditions))
          return (str_conditions, dynamodb_conditions))

      else:
          nodes[father_idx]["conditions"].append(f"({str_conditions})")
          nodes[father_idx]["dynamo_conditions"].append(reduce(operator, dynamo_conditions))

          
#LET'S TRY IT
query = {
        'AND': [
            {"k1": "v1"},
            {
                "OR": [
                    {"k2": "v2"},
                    {"k3": "v3"}
                ]
            },
            {
                "OR": [
                    {"k4": "v4"},
                    {"k5": "v5"}
                ]
            },
            {
                "AND": [
                    {"k6": "v8"},
                    {"k7": "v7"},
                    {
                        "OR": [
                            {"k8": "v8"},
                            {"k9": "v9"},
                            {
                                "AND": [
                                    {"k10": "v10"},
                                    {"k11": "v11"}
                                ]
                            }
                        ]
                    }
                ]

            }
        
        ]

    }
