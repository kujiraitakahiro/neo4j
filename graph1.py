#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from neo4j.v1 import GraphDatabase

driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password"))

def print_name(tx, name):
    for record in tx.run("MATCH (a:Person)-[:ACTED_IN]->(movie) WHERE a.name = $name "
                         "RETURN a.name ORDER BY a.name", name=name):
        print(record["a.name"])

with driver.session() as session:
    session.read_transaction(print_name, "Tom Hanks")


