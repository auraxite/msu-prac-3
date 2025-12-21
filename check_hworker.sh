#!/usr/bin/env bash

ST_A="Кибизов Кирилл"
ST_B="Броничев Александр"
TOML_PATH="personal.toml"

hworker $TOML_PATH -c update
hworker $TOML_PATH -c "show result" > test_data

grep "ID=${ST_A}.*USER_ID=${ST_A}" test_data || echo "Проверки тестов $ST_A на задачах $ST_A не было"
grep "ID=${ST_A}.*USER_ID=${ST_B}" test_data || echo "Проверки тестов $ST_B на задачах $ST_A не было"
grep "ID=${ST_B}.*USER_ID=${ST_A}" test_data || echo "Проверки тестов $ST_A на задачах $ST_B не было"
grep "ID=${ST_B}.*USER_ID=${ST_B}" test_data || echo "Проверки тестов $ST_B на задачах $ST_B не было"
