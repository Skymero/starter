Most recent Error:

Successfully installed deepskin-0.0.1
67202a3b001b871c2687
The path exists
The file exists
Image found
[ WARN:0@0.394] global loadsave.cpp:241 cv::findDecoder imread_('images/wound.png'): can't open/read file: check file path/integrity
Traceback (most recent call last):
  File "C:\Users\MartinezR\starter\src\manual_main.py", line 8, in <module>
    my_module.main(context)
  File "C:\Users\MartinezR\starter\src\main.py", line 114, in main
    wound_analysis = imp.load_source('wound_analysis', wound_analysis_path)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.10_3.10.3056.0_x64__qbz5n2kfra8p0\lib\imp.py", line 172, in load_source
    module = _load(spec)
  File "<frozen importlib._bootstrap>", line 719, in _load
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "C:\tmp\cloned_repo\WoundSize\WoundSize\wound_analysis.py", line 190, in <module>
    main("images/wound.png")
  File "C:\tmp\cloned_repo\WoundSize\WoundSize\wound_analysis.py", line 116, in main
    img = cv2.imread(f)[..., ::-1]
TypeError: 'NoneType' object is not subscriptable



