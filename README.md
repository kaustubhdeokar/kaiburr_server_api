# kaiburr_server_api
Task for Kaiburr internship selection

## PUT requests
`curl https://kaiburrtask1.herokuapp.com -XPUT -d '{"name": "Tornado server", "id": "125","language":"python","framework":"tornado"}'`
response - 
{"status": 201, "message": "server id 125 successfully"}

## GET requests
` curl -X GET https://kaiburrtask1.herokuapp.com`
response - {"status": 200, "message": "success", "servers": [{"name": "my centos", "id": "123", "language": "python", "framework": "django"}, {"name": "Tornado server", "id": "125", "language": "python", "framework": "tornado"}]}
