# Databricks notebook source
from runtime.nutterfixture import NutterFixture, tag
class MyTestFixture(NutterFixture):
        def run_test_table_populates(self):
            sqlContext.sql('DROP TABLE IF EXISTS key_players')
            dbutils.notebook.run('./TestingNotebook')
        
        def assertion_test_table_populates(self):
            playersTable = sqlContext.sql('SELECT Count(*) AS total From key_players')
            countValue = playersTable.first()[0]
            assert(countValue > 0)
result = MyTestFixture().execute_tests()
print(result.to_string())
result.exit(dbutils)

