#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from neo4j import GraphDatabase

driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password"))

def print_name(tx, name):
    for record in tx.run("MATCH (a:Person)-[:ACTED_IN]->(movie) WHERE a.name = $name "
                         "RETURN movie.name ORDER BY movie.name", name=name):
        print(record["movie.name"])

with driver.session() as session:
    session.read_transaction(print_name, "The Matrix")


