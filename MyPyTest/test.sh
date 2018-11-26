#!/usr/bin/env bash


allure_result_folder="./test_reports"

if [[ -n $1 ]]; then

    allure_result_folder=$@
fi

echo ${allure_result_folder}
behave -f allure_behave.formatter:AllureFormatter -o ${allure_result_folder} ./features

allure serve ${allure_result_folder}

