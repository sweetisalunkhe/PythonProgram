import argparse
import csv
import json
from collections import defaultdict


def get_params() -> dict:
    parser = argparse.ArgumentParser(description='DataTest')
    parser.add_argument('--customers_location', required=False, default="./input_data/starter/customers.csv")
    parser.add_argument('--products_location', required=False, default="./input_data/starter/products.csv")
    parser.add_argument('--transactions_location', required=False, default="./input_data/starter/transactions/")
    parser.add_argument('--output_location', required=False, default="./output_data/outputs/")
    return vars(parser.parse_args())


def read_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data


def read_json_lines(file_path):
    with open(file_path, 'r') as file:
        data = [json.loads(line) for line in file]
    return data


def write_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def preprocess_data(customers_file, transactions_file, products_file, output_file):
    customers = read_csv(customers_file)
    transactions = read_json_lines(transactions_file)
    products = read_csv(products_file)

    purchase_counts = defaultdict(int)

    for transaction in transactions:
        customer_id = transaction['customer_id']
        purchase_counts[customer_id] += 1

    preprocessed_data = []

    for customer in customers:
        customer_id = customer['customer_id']
        loyalty_score = int(customer['loyalty_score'])
        product_id = customer['product_id']

        product = next((p for p in products if p['product_id'] == product_id), None)

        if product:
            product_category = product['product_category']
        else:
            product_category = None

        count = purchase_counts[customer_id]

        data = {
            'customer_id': customer_id,
            'loyalty_score': loyalty_score,
            'product_id': product_id,
            'product_category': product_category,
            'purchase_count': count
        }

        preprocessed_data.append(data)

    write_json(preprocessed_data, output_file)


def main():
    params = get_params()
    customers_file = params['customers_location']
    transactions_file = params['transactions_location']
    products_file = params['products_location']
    output_file = params['output_location'] + 'preprocessed_data.json'

    preprocess_data(customers_file, transactions_file, products_file, output_file)


if __name__ == "__main__":
    main()
