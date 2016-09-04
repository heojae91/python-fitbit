# -*- coding: UTF-8 -*- 
import fitbit
import datetime

authd_client = fitbit.Fitbit('227SSP', '1b9a2c0936c02a7ad380db6885fcb4b1', access_token='eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI0VjdXNVkiLCJhdWQiOiIyMjdTU1AiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJzZXQgcmFjdCBybG9jIHJ3ZWkgcmhyIHJudXQgcnBybyByc2xlIiwiZXhwIjoxNDczMDQ5NjMwLCJpYXQiOjE0NzMwMjA4MzB9.E8iikajEMmgfXFDFFUgH1CXk1c6WOgvmNbteFmsKDZw', refresh_token='2523e4e4a5873ee87a48db44ebdf702a0827ce999108bae7f92d47c228f839c9')
result = authd_client.intraday_time_series('activities/steps', start_time='00:00', end_time='00:30')
print result