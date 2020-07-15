# optimize titles.json

In [Yari](https://github.com/mdn/yari), as a build step we produce a
`build/$locale/titles.json` file which get downloaded, with XHR, in
the browser so it matters that it's not unnecessarily big which means
due to network speed would be bad user experience.

## To run the experiment

Run:

    python 1.py  # generates 1.json
    python 2.py  # genetates 2.csv
    python 3.py  # generates 4.json
    python 4.py  # generates 4.json

Produce the table with:

    python table.py

Or just use `ls`:

    ls -ltrS

## Results

One version of the results as of today:

![](./graph.png)
