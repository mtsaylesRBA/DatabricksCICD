# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE key_players (
# MAGIC     player_name VARCHAR(255),
# MAGIC     team VARCHAR(255)
# MAGIC );
# MAGIC
# MAGIC INSERT INTO key_players (player_name, team) VALUES
# MAGIC ('Aaron Rodgers', 'Green Bay Packers'),
# MAGIC ('Tom Brady', 'Tampa Bay Buccaneers'),
# MAGIC ('Patrick Mahomes', 'Kansas City Chiefs'),
# MAGIC ('Derrick Henry', 'Tennessee Titans'),
# MAGIC ('DeAndre Hopkins', 'Arizona Cardinals'),
# MAGIC ('Barry Sander', 'Detroit Lions');
