from fastapi import FastAPI, Request, Response, HTTPException, status

app = FastAPI()

players_online = []


@app.post('/update_online')
async def update_online(request: Request):
    data = await request.json()
    players = data.get('players', [])

    if not isinstance(players, list):
        raise HTTPException(status_code=400, detail="Invalid data format. 'players' should be a list.")

    global players_online
    players_online = players
    print("POST", len(players_online))
    return {"message": "Players online updated successfully"}


@app.get('/get_online')
async def get_online():
    print("GET", players_online)
    return players_online
