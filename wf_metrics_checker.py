import tkinter as tk

#Wavefront metric limits checking tool. Contact htahir@vmware.com for questions

# Function that checks char limit for metric and displays results
def check_metric():
    get_metric = em.get()
    metric_len = len(get_metric)
    if metric_len > 256:
        text_mb = ("   Metric length is {}. It will be rejected by Wavefront!   ").format(metric_len)
        error_metric = tk.Label(master=root, text=text_mb).grid(row=4, column=1)
        metric_red = tk.Label(master=root, text="Reduce length", bg="red").grid(row=4, column=2)
    else:
        text_mg = ("Metric length is {}. Metric name length is within the limit ").format(metric_len)
        good_metric = tk.Label(master=root, text=text_mg).grid(row=4, column=1)
        metric_green = tk.Label(master=root, text="Success", bg="lightgreen").grid(row=4, column=2)

# Function that checks source name char limits and displays Results
def check_source():
    get_source = es.get()
    source_len = len(get_source)
    if source_len > 128:
        text_sb = ("Source length is {}. Metric will be rejected due to source name exceeding limit!").format(source_len)
        error_source = tk.Label(master=root, text=text_sb).grid(row=6, column=1)
        source_red = tk.Label(master=root, text="Reduce length", bg="red").grid(row=6, column=2)
    else:
        text_sg = ("Source length is {}. Source name is within the limit").format(source_len)
        good_source = tk.Label(master=root, text=text_sg).grid(row=6, column=1)
        source_green = tk.Label(master=root, text="Success", bg="lightgreen").grid(row=6, column=2)

# Function that checks point tag key limits
def check_pkey():
    get_pkey = epk.get()
    pk_len = len(get_pkey)
    if pk_len > 64:
        text_pkb = ("Point tag key length is {}. The metric will be rejected due to point tag key exceeding limit!").format(pk_len)
        error_key = tk.Label(master=root, text=text_pkb).grid(row=8, column=1)
        key_red = tk.Label(master=root, text="Reduce length", bg="red").grid(row=8, column=2)
    else:
        text_pkg = ("Point tag key length is {}. Point tag key is within the limit").format(pk_len)
        good_key = tk.Label(master=root, text=text_pkg).grid(row=8, column=1)
        key_green = tk.Label(master=root, text="Success", bg="lightgreen").grid(row=8, column=2)

# Function that checks point tag value limits
def check_pvalue():
    get_pv = epv.get()
    pv_len = len(get_pv)
    if pv_len > 255:
        text_pvb = ("Point tag value length is {}. Metric will be rejected due to point tag value exceeding limit!").format(pv_len)
        error_value = tk.Label(master=root, text=text_pvb).grid(row=10, column=1)
        error_red = tk.Label(master=root, text="Reduce length", bg="red").grid(row=10, column=2)
    else:
        text_pvg = ("Point tag value's length is {}. Point tag value is within the limit").format(pv_len)
        good_value = tk.Label(master=root, text=text_pvg, pady=10).grid(row=10, column=1)
        value_green = tk.Label(master=root, text="Success", bg="lightgreen").grid(row=10, column=2)


#Tkinter GUI setup

root = tk.Tk()
root.title("Metrics Checker | htahir@vmware.com")

root.columnconfigure([0, 1, 2], minsize=70, weight=1)


# Title and about the tool

title = tk.Label(root, width=25, bg="lightblue", text="Wavefront Metrics Checker", font=('Helvetica', 18, 'bold')).grid(row=0, column=1)
tagline = tk.Label(root, text="Use this tool to verify your metrics conform to Wavefront backend limits").grid(row=1, column=1, padx=10)

extra_space = tk.Label(root).grid(row=2, column=1, pady=10)


# Input for metric name
enter_m = tk.Label(root, text="Metric Name:\nLimit 256").grid(row=3, column=0, padx=10)
em = tk.Entry(width=100)
em.grid(row=3, column=1, padx=1, pady=10)

metric_button = tk.Button(master=root, text="Check Metric", command=check_metric, width=20, height=1).grid(row=3, column=2, padx=10)

# Input for source Name
enter_s = tk.Label(root, text="Source Name:\nLimit 128").grid(row=5, column=0, padx=10)
es = tk.Entry(width=100)
es.grid(row=5, column=1, padx=1, pady=10)

source_button = tk.Button(master=root, text="Check Source", command=check_source, width=20, height=1).grid(row=5, column=2, padx=10)

#Input for point tag key
enter_pk = tk.Label(root, text="Point Tag Key:\nLimit 64").grid(row=7, column=0, padx=10)
epk = tk.Entry(width=100)
epk.grid(row=7, column=1, padx=1, pady=10)

key_button = tk.Button(master=root, text="Check Point Tag Key", command=check_pkey, width=20, height=1).grid(row=7, column=2, padx=10)

#Input for point tag key
enter_pv = tk.Label(root, text="Point Tag Value:\nLimit 255").grid(row=9, column=0, padx=10)
epv = tk.Entry(width=100)
epv.grid(row=9, column=1, padx=1, pady=10)

value_button = tk.Button(master=root, text="Check Point Tag Value", command=check_pvalue, width=20, height=1).grid(row=9, column=2, padx=10)


extra_space1 = tk.Label(root, text="________________________________________version_1.0____________________________________________\nhttps://docs.wavefront.com/wavefront_limits.html#default-customer-specific-limits").grid(row=11, column=1, pady=10)


root.mainloop()
