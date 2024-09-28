import requests
import time

# Function to get the home run data for top players
def get_top_hitters_home_runs():
    # API Endpoint - replace with the actual endpoint and your API key
    url = "https://api.example.com/baseball/stats/homeruns"  # Hypothetical API endpoint
    headers = {
        'Authorization': 'Bearer YOUR_API_KEY'  # If the API requires an API key
    }
    
    # Send a request to the API to get the home run data
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        # Parse JSON data
        data = response.json()
        
        # Example: Iterate through top hitters and print their home run counts
        top_hitters = data['players']  # Assuming data has a "players" key
        
        print(f"{'Player':<20} {'Home Runs':<10}")
        print("-" * 30)
        for player in top_hitters:
            name = player['name']
            home_runs = player['home_runs']
            print(f"{name:<20} {home_runs:<10}")
    else:
        print("Failed to retrieve data:", response.status_code)

# Track home runs continuously (e.g., check every 30 minutes)
def track_home_runs(interval=1800):
    while True:
        print("\nFetching updated home run data...")
        get_top_hitters_home_runs()
        print("\nWaiting for next update...\n")
        time.sleep(interval)  # Wait for the interval before checking again

# Main function to start tracking
if __name__ == "__main__":
    track_home_runs(interval=1800)  # Fetch data every 30 minutes
