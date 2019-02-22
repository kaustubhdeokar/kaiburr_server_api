# kaiburr_server_api
Task for Kaiburr internship selection 
By Kaustubh Deokar(16BCE0353)


## PUT requests
`curl https://kaiburrtask1.herokuapp.com -XPUT -d '{"name": "Tornado server", "id":"125","language":"python","framework":"tornado"}'`
<br>response - 
{"status": 201, "message": "server id 125 successfully"}

## GET requests
` curl -X GET https://kaiburrtask1.herokuapp.com`
<br>response - {"status": 200, "message": "success", "servers": [{"name": "my centos", "id": "123", "language": "python", "framework": "django"}, {"name": "Tornado server", "id": "125", "language": "python", "framework": "tornado"}]}
<br>
<br>
`curl -X GET https://kaiburrtask1.herokuapp.com?123`
<br>
{"status": 200, "message": "success","servers":{"name": "my centos", "id": "123", "language": "python", "framework": "django"}}
<br>
`curl -X GET https://kaiburrtask1.herokuapp.com?123`
<br>
{"status": 404, "message": "no servers"}
<br>

## DELETE requests
`curl -X DELETE https://kaiburrtask1.herokuapp.com?id=124`
{"status": 202, "message": "successfully deleted"}
`curl -X DELETE https://kaiburrtask1.herokuapp.com?id=999`
{"status":503, "message": "id not registered"}
