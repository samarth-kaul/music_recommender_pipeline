from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../ingestion')))

from ingestion.spotify_client import SpotifyClient
import snowflake.connector
from dotenv import load_dotenv

load_dotenv()

SPOTIFY_ARTISTS = ["Taylor Swift", "One Republic", "Drake", "Imagine Dragons", "Maroon 5", "Demi Lovato"]



