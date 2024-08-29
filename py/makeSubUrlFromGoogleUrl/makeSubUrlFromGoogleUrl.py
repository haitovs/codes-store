def convert_to_direct_downloads(file_id):
    # Construct both Google Drive and Usercontent direct download links
    google_drive_url = f"https://drive.google.com/uc?export=download&id={file_id}"
    usercontent_url = f"https://drive.usercontent.google.com/uc?export=download&id={file_id}"
    return google_drive_url, usercontent_url

def extract_file_id(url):
    try:
        if "drive.google.com/file/d/" in url:
            return url.split("/d/")[1].split("/")[0]
        elif "uc?export=download&id=" in url:
            return url.split("id=")[1]
        else:
            return None
    except IndexError:
        return None

def read_and_convert_urls(file_name):
    try:
        # Open the file in read mode
        with open(file_name, 'r') as file:
            lines = file.readlines()

        converted_results = []

        # Process each line in the file
        for line in lines:
            url, name = map(str.strip, line.split(',', 1))  # Split by the first comma, strip whitespace
            file_id = extract_file_id(url)

            if file_id:
                google_drive_url, usercontent_url = convert_to_direct_downloads(file_id)
                # Add the result for both Google Drive and Usercontent
                converted_results.append((name, google_drive_url, usercontent_url))
            else:
                converted_results.append((name, "Invalid URL", "Invalid URL"))

        return converted_results

    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def save_results_to_file(results, output_file):
    try:
        # Write the results to a file
        with open(output_file, 'w') as file:
            for name, google_drive_url, usercontent_url in results:
                file.write(f"{name}: {google_drive_url}\n")
            file.write("\n")
            for name, google_drive_url, usercontent_url in results:
                file.write(f"{name}: {usercontent_url}\n")
    except Exception as e:
        print(f"Error saving to file: {e}")

def main():
    # Specify the input and output file names
    input_file = "targets.txt"
    output_file = "result.txt"

    # Read the URLs and convert them
    converted_results = read_and_convert_urls(input_file)

    # Show the results in the console
    if converted_results:
        print("Here are the converted URLs with names:")
        for name, google_drive_url, usercontent_url in converted_results:
            print(f"{name}: {google_drive_url}")
        print("\n")
        for name, google_drive_url, usercontent_url in converted_results:
            print(f"{name}: {usercontent_url}")

        # Save the results to a file
        save_results_to_file(converted_results, output_file)

        print(f"\nThe results have been saved to '{output_file}'.")
    else:
        print("No URLs found or an error occurred.")

if __name__ == "__main__":
    main()
