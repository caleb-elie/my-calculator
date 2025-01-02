const display = document.getElementById('display');

        function appendNumber(number) {
            display.value += number;
        }

        function appendOperator(operator) {
            if (display.value && !isNaN(display.value.slice(-1))) {
                display.value += operator;
            }
        }

        function clearDisplay() {
            display.value = '';
        }

        function calculateResult() {
            try {
                display.value = eval(display.value);
            } catch (error) {
                display.value = 'Error';
            }
        }