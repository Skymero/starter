Most recent Error:

 tzdata-2024.2 wcwidth-0.2.13 webencodings-0.5.1
Obtaining file:///C:/tmp/cloned_repo/WoundSize/WoundSize/Deepskin
  Installing build dependencies ... done
  Checking if build backend supports build_editable ... done
  Getting requirements to build editable ... done
  Preparing editable metadata (pyproject.toml) ... done
Building wheels for collected packages: deepskin
  Building editable for deepskin (pyproject.toml) ... done
  Created wheel for deepskin: filename=deepskin-0.0.1-0.editable-py3-none-any.whl size=12319 sha256=b6016922f605f7ffe635d2101a25d20a0d5941bf010ae39f7bcee142d38a3a70
  Stored in directory: C:\Users\MartinezR\AppData\Local\Temp\pip-ephem-wheel-cache-241m_oo_\wheels\6f\46\98\36f605e655e2a1861c85a9f12884094dd85be4ac2b083b1df7
Successfully built deepskin
Installing collected packages: deepskin
Successfully installed deepskin-0.0.1
67202a3b001b871c2687
Traceback (most recent call last):
  File "C:\Users\MartinezR\starter\src\main.py", line 90, in main
    import wound_analysis as image_processor  # Dynamically importing the cloned module
  File "C:\tmp/cloned_repo/WoundSize/WoundSize\wound_analysis.py", line 4, in <module>
    from deepskin import wound_segmentation
ModuleNotFoundError: No module named 'deepskin'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\MartinezR\starter\src\manual_main.py", line 8, in <module>
    my_module.main(context)
  File "C:\Users\MartinezR\starter\src\main.py", line 113, in main
    context.error(f"Image processing failed: {repr(err)}")
AttributeError: 'dict' object has no attribute 'error'
