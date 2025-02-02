from typing import List, Optional

from flask import Flask, request

app = Flask(__name__)

# /search/3/12/2/1/1/999*/2/2G/4G/1/-100 - плохо


@app.route("/search", methods=["GET"],
)
def search():
    cell_tower_ids: List[int] = request.args.getlist("cell_tower_id", type=int)
    
    if not cell_tower_ids:
        return "You must specify at least one cell_tower_id", 400
    
    phone_prefixes: List[str] = request.args.getlist("phone_prefix")
    protocols: List[str] = request.args.getlist("protocol")
    
    signal_level: Optional[float] = request.args.get("signal_level", type=float, default=None)
    
    return {
        "Search for": f"{cell_tower_ids} cell towers. Search criteria:",
        "phone_prefixes": phone_prefixes,
        "protocols": protocols,
        "signal_level": signal_level
    }

if __name__ == "__main__":
    app.run(debug=True)