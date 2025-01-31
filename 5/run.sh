# run.sh
#!/bin/bash

# Run the test
npm test
EVAL_EXIT_CODE=$?

# Exit the script
exit $EVAL_EXIT_CODE