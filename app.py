from flask import Flask, request, jsonify

app = Flask(__name__)

FULL_NAME = "john_doe"
DOB = "17091999"  
EMAIL = "john@xyz.com"
ROLL_NUMBER = "ABCD123"


def process_data(data):
    even_numbers = []
    odd_numbers = []
    alphabets = []
    special_characters = []
    total_sum = 0
    alpha_concat = []

    for item in data:
        if item.isdigit():  
            num = int(item)
            if num % 2 == 0:
                even_numbers.append(item)
            else:
                odd_numbers.append(item)
            total_sum += num
        elif item.isalpha(): 
            alphabets.append(item.upper())
            alpha_concat.append(item)
        else:
            special_characters.append(item)

    concat_string = ""
    rev = "".join(alpha_concat)[::-1]
    for i, ch in enumerate(rev):
        concat_string += ch.upper() if i % 2 == 0 else ch.lower()

    return {
        "is_success": True,
        "user_id": f"{FULL_NAME}_{DOB}",
        "email": EMAIL,
        "roll_number": ROLL_NUMBER,
        "odd_numbers": odd_numbers,
        "even_numbers": even_numbers,
        "alphabets": alphabets,
        "special_characters": special_characters,
        "sum": str(total_sum),
        "concat_string": concat_string
    }


@app.route("/bfhl", methods=["POST"])
def bfhl():
    try:
        data = request.json.get("data", [])
        result = process_data(data)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True)
