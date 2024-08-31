# I/O Movement in BeeGFS

## Level 1

In the first paper analyses the I/O performance of BeeGFS on different workloads by <br />
1. Using two different allocation strategies, <br />
2. Varying strip count and chunk size.

The first test finds that both the default random allocation and the round-robin allocation lead to data imbalance at the OST levels. It also leads to CPU load imbalance at the OSS level, but no such trend was seen for Memory consumption for the servers. <br />
In the second test four parameters were measured, Read and Write Throughput and Read and Write Latency. It was found that the default striping pattern, (4, 512 KiB) where 4 is the stripe count and 512 Kib is the chunk size, again behaves sub-optimally, especially for small files. When subjected to concurrent workloads with three different benchmarks, all three of them performed best with different striping patterns, none of which were the default pattern. <br />
The study concludes that default OST allocation strategies cause load imbalance and default striping patterns give sub-optimal results in some workloads. It concludes that a more flexible striping configuration is required based on the I/O characteristics of the workloads.


In the second paper, section 2, the multi-layered software stack involved in I/O in HPC systems is described. In general the authors observe that complex layers of the software stack leads to excessive abstraction and thus loss of contexual data of the I/O requests.

## Level 2

I had some problems installing DLIO on my Mac. I tried the installations using `pip` in a virtual env's but it kept failing while trying to install `nvidia-dali-cuda110`. Maybe its obvious that it doesn't work since there's no Nvidia GPU on this machine, but regardless I looked it up and maybe [this is the issue?](https://developer.nvidia.com/nvidia-cuda-toolkit-11_7_0-developer-tools-mac-hosts). But [here](https://dlio-benchmark.readthedocs.io/en/latest/testedsystems.html) they mention MacOS so I'm not sure what the problem is. I tried the same thing on my second computer which has an Nvidia GPU, running Zorin OS 17 x86_64, and it worked. I ran `mpirun -np 4 dlio_benchmark workload=unet3d ++workload.workflow.generate_data=True ++workload.workflow.train=False` and `mpirun -np 4 dlio_benchmark workload=default`. The logs from them have been uploaded. `dlio_postprocessor` failed however.

## Level 3
I'm yet to read about Darshan.