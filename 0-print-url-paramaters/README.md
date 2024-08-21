# Print URL Parameters

## Prompt
    Hi Chat!  I'm working on a project that uses pre-filled URLs, specifically, the URLs contain two dates in the format:


    ```
    example.com/?o=1234567890&p_billing_month=2021-08-01&p_compare_month=2021-07-01
    ```

    I would like to create a python script that lets me select the `p_billing_month` and `p_billing_month` parameters by passing in arguments. 

    The script should then print the URL with the arguments in the correct format.

    For example, I'd like to enter:

    ```
    script.py --target=2024-07-01 --compare=2024-06-01
    ```

    The script should print:

    ```
    example.com/?o=1234567890&p_billing_month=2024-07-01&p_compare_month=2024-06-01
    ```

    If no value is entered for the `--target` argument, the script should use the current year and month (day will always be "01").

    In addition, if no value is entered for the `--compare` argument, the script should use the month prior to the value entered or calcuated for the target month.

    Lastly, add a `--help` parameter that prints information on how to use the script with the arguments as explained here.

    If a python library can implement this, please use the libary versus implementing these features from scratch.

## GPT 4o

|Max Tokens|Temperature|Top P|
|----------|-----------|-----|
|512       |1          |1    |

TTFT: 702 ms
Time:  6503 ms
Input: 300 tkns
Output: 512 tkns
Cost: $0.009

## Llama 3.1 8B Instruct

|Max Tokens|Temperature|Top P|
|----------|-----------|-----|
|512       |0.5        |0.9  |

TTFT: 260 ms
Time: 5369 ms
Input: 304 tkns
Output: 501 tkns
Cost: $0.0004

## Claude 3.5 Sonnet

|Max Tokens|Temperature|Top P|
|----------|-----------|-----|
|600       |1          |0.999|

TTFT: 855 ms
Time: 10118 ms
Input: 329 tkns
Output: 599 tkns
Cost: $0.01

## Mixtral 8x7B Instruct

|Max Tokens|Temperature|Top P|
|----------|-----------|-----|
|512       |0.5        |0.9. |

TTFT: 179 ms
Time: 6502 ms
Input: 396 tkns
Output: 512 tkns
Cost: $0.0005

