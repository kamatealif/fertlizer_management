# Fertilizer Management System

This is a **Fertilizer Management System** built using **Flask, Pandas, and Excel**. It allows users to record fertilizer usage, view the number of records in the database, and download the data as an Excel file.

## Features
- Add new fertilizer records (customer name, date, fertilizer type, quantity, cost).
- Store data in an Excel file (`fertilizer_data.xlsx`).
- View a summary of the number of rows and columns.
- Download the Excel file containing all entries.

## Requirements
Ensure you have Python installed along with the following dependencies:

```sh
pip install flask pandas openpyxl
```

## How to Run
1. Clone this repository or copy the files to your project directory.
2. Run the Flask app:
   
   ```sh
   python app.py
   ```
3. Open your browser and go to:
   
   ```
   http://127.0.0.1:5000/
   ```

## Endpoints
| Route         | Method | Description |
|--------------|--------|-------------|
| `/`          | GET    | Displays the homepage |
| `/add`       | POST   | Adds a new fertilizer record |
| `/report`    | GET    | Shows the number of rows and columns |
| `/download`  | GET    | Downloads the Excel file |

## File Structure
```
project_folder/
│── app.py            # Flask backend
│── templates/
│   ├── index.html    # Home page with form
│   ├── report.html   # Report page with summary & download button
│── static/
│   ├── style.css     # Styling for the web pages
│── fertilizer_data.xlsx  # Excel file storing records
```

## Notes
- The system automatically creates `fertilizer_data.xlsx` if it doesn’t exist.
- Ensure `openpyxl` is installed to handle Excel files.

## License
This project is open-source and free to use.

---
**Happy Coding! 🚀**