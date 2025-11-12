Implementation of using of basic actions and assertions in Playwright (Python).  
This test automation framework was taken as a basis: https://github.com/Somatori/web_taf_python_pytest_playwright

## Reporting with Allure

The **Allure** is used for rich HTML reports (attachments, history, etc).

Running tests with report generation:

```bash
ALLURE_AUTO_GENERATE=1 pytest -q --alluredir=artifacts/allure-results
# or for running tests in parallel
ALLURE_AUTO_GENERATE=1 pytest -q -n 2 --alluredir=artifacts/allure-results
```

Opening the generated report:

```bash
allure open artifacts/allure-report
```

## Trace tests

Tracing is generated at `artifacts/traces` if the test is failed (by default).

To view the trace run:

```bash
playwright show-trace artifacts/traces/<your-trace-file>.zip
# or
python -m playwright show-trace artifacts/traces/<your-trace-file>.zip
```
