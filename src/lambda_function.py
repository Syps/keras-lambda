from __future__ import print_function
import os


if os.environ.get('LAMBDA_TASK_ROOT') is None:
    print("just exit, we are not in a lambda function"),
    import sys
    sys.exit(0)

import json
import numpy as np
import tempfile
import time
import h5py


def lambda_handler(event, context):
    my_array = np.ones((2, 2))
    model = h5py.File('model.h5', 'r')

    print('loaded model!')

    handler_start_time = time.time()
    start_time = time.time()

    end_time = time.time()

    outputs = []

    print('Predicted: {}'.format(outputs))
    h_time = end_time - handler_start_time
    p_time = end_time - start_time
    print("handler: {} pred time: {}".format(h_time, p_time))

    out = {
            "headers": {
                "content-type": "application/json",
                "Access-Control-Allow-Origin": "*"
                },
            "body": '{"result":"success!"}',
            "statusCode": 200
          }

    return out