from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

data_store = {
    "previous_month_revenue": 500000,  # 前月の収益
    "investment_info": [],
}

def calculate_distribution(profit, distribution_percentage):
    return round(profit * distribution_percentage, 2)

def calculate_staking_reward(individual_distribution, reward_rate):
    return round(individual_distribution * reward_rate, 2)

@app.route('/api/predict_revenue', methods=['GET'])
def predict_revenue():
    previous_revenue = data_store["previous_month_revenue"]
    predicted_revenue = round(previous_revenue * 1.1, 2)  # 10%増加の仮定
    return jsonify({"predicted_revenue": predicted_revenue})

@app.route('/api/invest', methods=['POST'])
def invest():
    try:
        investment_amount = float(request.json.get('investment_amount'))  # 投資額
        stake_years = int(request.json.get('stake_years'))  # ステーキング期間
        distribution_percentage = float(request.json.get('distribution_percentage')) / 100  # 分配率(%)

        reward_rate = 1.05 + 0.05 * (stake_years - 1)  # 年数に応じた報酬率
        predicted_revenue = data_store["previous_month_revenue"] * 1.1  # 前月の収益に10%増加を仮定
        total_expenses = predicted_revenue * 0.6  # 60%をコストと仮定
        total_profit = predicted_revenue - total_expenses

        # 分配額の計算
        distribution_profit = calculate_distribution(total_profit, distribution_percentage)
        individual_distribution = round(distribution_profit * (investment_amount / predicted_revenue), 2)

        # ステーキング報酬の計算
        staking_reward = calculate_staking_reward(individual_distribution, reward_rate)

        # 投資情報の保存
        investment_record = {
            "investment_amount": investment_amount,
            "stake_years": stake_years,
            "distribution_percentage": distribution_percentage * 100,  # 元の%形式に戻す
            "reward_rate": reward_rate,
            "individual_distribution": individual_distribution,
            "staking_reward": staking_reward
        }
        data_store["investment_info"].append(investment_record)

        return jsonify({"message": "Investment successful", "staking_reward": staking_reward})

    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/investment_data', methods=['GET'])
def get_investment_data():
    return jsonify({"investment_info": data_store["investment_info"]})

if __name__ == '__main__':
    app.run(debug=True)