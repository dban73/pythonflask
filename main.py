import server
import route.persona_route

if __name__ == "__main__":
    server.app.run(host='0.0.0.0',port='8040', debug=True)