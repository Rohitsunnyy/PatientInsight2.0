# PatientInsight

PatientInsight is an MLOps project for patient care and diagnosis assistance using the PMC-Patients dataset.

## Project Structure

[Explain the project structure here]

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/patientinsight.git
   cd patientinsight
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up DVC:
   ```
   dvc init
   dvc remote add -d myremote /path/to/remote/storage
   ```

5. Set up Airflow:
   ```
   export AIRFLOW_HOME=$(pwd)/airflow
   airflow db init
   airflow users create --username admin --password admin --firstname Admin --lastname User --role Admin --email admin@example.com
   ```

## Usage

1. Download the dataset:
   ```
   python patientinsight/data/download.py
   ```

2. Preprocess the data:
   ```
   python patientinsight/data/preprocess.py
   ```

3. Run tests:
   ```
   pytest
   ```

4. Start Airflow webserver and scheduler:
   ```
   airflow webserver -p 8080
   airflow scheduler
   ```

5. Access the Airflow web interface at `http://localhost:8080` and trigger the `patientinsight_pipeline` DAG.

## Contributing

[Explain how to contribute to the project]

## License

[Include license information]
