# CriptPerformance
Pyhton program that mesures the performance of cryptography methods

# How to run

First make sure you have python3 installed in your machine then install the module cryptography.
You can do that using the pip command.
```console
pip install cryptography
```

Then cd into src and run
```console
python main.py
```

# Exemple output

<pre>
-------------STATIC TEXT FILES-------------

aes_256_ctr (number of runs = 5000) : 

************************************************************************************************
|  input size(bytes)  |  avg encryption time per run (μs)  | avg decryption time per run (μs)  |
|        2            |               --                   |              --                   |
|        4            |               --                   |              --                   |
|        8            |             61.0176                |            58.0758                |
|        16           |               --                   |              --                   |
|        32           |               --                   |              --                   |
|        64           |             60.7534                |            57.9767                |
|        128          |               --                   |              --                   |
|        512          |             61.0729                |            58.3067                |
|        4096         |             63.7366                |            60.5437                |
|        32768        |             83.1316                |            79.8322                |
|        262144       |             203.5673               |            196.4983               |
|        2047152      |             1645.7208              |            1640.7556              |
************************************************************************************************

rsa (number of runs = 5000) : 

************************************************************************************************
|  input size(bytes)  |  avg encryption time per run (μs)  | avg decryption time per run (μs)  |
|        2            |             159.8787               |            817.8524               |
|        4            |             151.6421               |            794.6952               |
|        8            |             166.4346               |            884.2143               |
|        16           |             166.6630               |            896.2929               |
|        32           |             166.7340               |            911.8126               |
|        64           |             178.5857               |            938.9900               |
|        128          |             168.8417               |            918.7277               |
|        512          |               --                   |              --                   |
|        4096         |               --                   |              --                   |
|        32768        |               --                   |              --                   |
|        262144       |               --                   |              --                   |
|        2047152      |               --                   |              --                   |
************************************************************************************************

sha256 (number of runs = 5000) : 

************************************************************************************************
|  input size(bytes)  |  avg encryption time per run (μs)  | avg decryption time per run (μs)  |
|        2            |               --                   |              --                   |
|        4            |               --                   |              --                   |
|        8            |             12.7234                |              --                   |
|        16           |               --                   |              --                   |
|        32           |               --                   |              --                   |
|        64           |             12.9334                |              --                   |
|        128          |               --                   |              --                   |
|        512          |             15.9314                |              --                   |
|        4096         |             26.1410                |              --                   |
|        32768        |             114.4097               |              --                   |
|        262144       |             837.8878               |              --                   |
|        2047152      |             6201.0247              |              --                   |
************************************************************************************************

-------------GENERATED TEXT FILES-------------

aes_256_ctr (number of runs = 5000) : 

************************************************************************************************
|  input size(bytes)  |  avg encryption time per run (μs)  | avg decryption time per run (μs)  |
|        2            |               --                   |              --                   |
|        4            |               --                   |              --                   |
|        8            |             65.6197                |            61.7846                |
|        16           |               --                   |              --                   |
|        32           |               --                   |              --                   |
|        64           |             65.6408                |            61.5296                |
|        128          |               --                   |              --                   |
|        512          |             70.4494                |            66.4881                |
|        4096         |             68.9991                |            64.8033                |
|        32768        |             80.0075                |            76.2940                |
|        262144       |             208.6307               |            201.2543               |
|        2047152      |             1624.7138              |            1612.1392              |
************************************************************************************************

rsa (number of runs = 5000) : 

************************************************************************************************
|  input size(bytes)  |  avg encryption time per run (μs)  | avg decryption time per run (μs)  |
|        2            |             135.1554               |            757.4853               |
|        4            |             162.4293               |            862.0442               |
|        8            |             177.9361               |            922.9211               |
|        16           |             177.6254               |            930.9049               |
|        32           |             173.1755               |            908.7736               |
|        64           |             173.1383               |            921.6228               |
|        128          |             168.4430               |            905.7629               |
|        512          |               --                   |              --                   |
|        4096         |               --                   |              --                   |
|        32768        |               --                   |              --                   |
|        262144       |               --                   |              --                   |
|        2047152      |               --                   |              --                   |
************************************************************************************************

sha256 (number of runs = 5000) : 

************************************************************************************************
|  input size(bytes)  |  avg encryption time per run (μs)  | avg decryption time per run (μs)  |
|        2            |               --                   |              --                   |
|        4            |               --                   |              --                   |
|        8            |             13.1700                |              --                   |
|        16           |               --                   |              --                   |
|        32           |               --                   |              --                   |
|        64           |             13.4794                |              --                   |
|        128          |               --                   |              --                   |
|        512          |             14.7838                |              --                   |
|        4096         |             25.8035                |              --                   |
|        32768        |             118.2388               |              --                   |
|        262144       |             798.4610               |              --                   |
|        2047152      |             6148.1540              |              --                   |
************************************************************************************************

</pre>

# Static text graph
![static](https://user-images.githubusercontent.com/71783901/191142241-ebc2d9ae-d76d-4df4-8ebd-a52439a1c06e.png)

# Generated text graph
![generated](https://user-images.githubusercontent.com/71783901/191142286-50ffe60d-43cc-442b-b071-185d7dc660dd.png)






