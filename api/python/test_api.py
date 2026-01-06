import requests
import base64
import os

def test_api():
    try:
        # Check if test image exists
        if not os.path.exists('test.jpg'):
            print("Error: test.jpg not found! Please add a test image.")
            return

        # Read and encode image
        print("Reading image file...")
        with open('test.jpg', 'rb') as image_file:
            base64_image = base64.b64encode(image_file.read()).decode('utf-8')
        
        print("Sending request to API...")
        url = 'https://my-personal-website-t7tw.onrender.com/api/analyze'
        response = requests.post(
            url,
            json={'image': base64_image},
            headers={'Content-Type': 'application/json'}
        )
        
        print(f"Status Code: {response.status_code}")
        
        if response.ok:
            print("Success!")
            print("Response:", response.json())
        else:
            print("Error!")
            print("Response:", response.text)
            
    except Exception as e:
        print(f"Error occurred: {str(e)}")

if __name__ == "__main__":
    test_api() 