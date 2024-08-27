def convert_to_direct_download(url):
    try:
        # Extract the file ID from the original Google Drive link
        if "drive.google.com/file/d/" in url:
            file_id = url.split("/d/")[1].split("/")[0]
            # Construct the direct download link
            download_url = f"https://drive.google.com/uc?export=download&id={file_id}"
            return download_url
        else:
            return "Invalid Google Drive URL"
    except IndexError:
        return "Invalid format for Google Drive link"

def read_and_convert_urls(file_name):
    try:
        # Open the file in read mode
        with open(file_name, 'r') as file:
            lines = file.readlines()

        converted_results = []

        # Process each line in the file
        for line in lines:
            url, name = map(str.strip, line.split(',', 1))  # Split by the first comma, strip whitespace
            converted_url = convert_to_direct_download(url)
            converted_results.append((name, converted_url))

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
            for name, url in results:
                file.write(f"{name}: {url}\n")
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
        for name, url in converted_results:
            print(f"{name}: {url}")

        # Save the results to a file
        save_results_to_file(converted_results, output_file)

        print(f"\nThe results have been saved to '{output_file}'.")
    else:
        print("No URLs found or an error occurred.")

if __name__ == "__main__":
    main()
