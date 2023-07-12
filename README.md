# JSON-to-CSV-Converter

This code is a simple Python script that converts JSON data into a CSV (Comma-Separated Values) file. It utilizes the `json` and `pandas` libraries to accomplish the task.

## Prerequisites
- Python 3.x
- `json` library
- `pandas` library

## Usage
1. Make sure you have Python 3.x installed on your system.
2. Install the required libraries by running the following command:
   ```shell
   pip install pandas
   ```
3. Save the JSON file you want to convert to a CSV file.
4. Update the `json_file` variable with the path to your JSON file.
5. Run the script using the following command:
   ```shell
   python json_to_csv.py
   ```
6. After execution, the resulting CSV file will be saved in the specified location (`C:\Users\Peace\data.csv` in the provided code).

Note: It's important to ensure that the JSON file is in a valid format and matches the expected structure. Otherwise, the script may raise errors.

## Customization
- If your JSON file is located in a different directory, modify the `json_file` variable with the appropriate path.
- If you want to change the output CSV file name or location, update the `to_csv` method's argument in the last line of the script (`df.to_csv("output.csv", index=False)`).

## FAQ
### Can I follow you on your social media platforms ? 

Yes you can !
 
 You'll find me 
- Posting memes or talking about data on [Twitter](https://twitter.com/LowCodeDataGirl/status/1539491369491759107?s=20&t=_AIGHnY6mDlG9uaiR8aa0g)
- Writing articles about complex data concepts and making them digestible on [Medium](lowcodedatagirl.medium.com)   
- Posting data vizualizations inspiration and data infographics on [Instagram](https://www.instagram.com/lowcodedatagirl/)

## License

Distributed under the no License. See LICENSE.txt for more information.

## Show Your Support
Please ⭐️ this repository if this project helped you or [buy me coffee]( https://www.buymeacoffee.com/lowcodedatagirl)!
