---
title: nvidia-smi
---

## nvidia-smi
NVIDIA System Management Interface.

NVSMI provides monitoring information for Tesla and select Quadro devices.
The data is presented in either a plain text or an XML format, via stdout or a file.
NVSMI also provides several management operations for changing the device state.

Note that the functionality of NVSMI is exposed through the NVML C-based
library. See the NVIDIA developer website for more information about NVML.
Python wrappers to NVML are also available.  The output of NVSMI is
not guaranteed to be backwards compatible; NVML and the bindings are backwards
compatible.

Supported products:
- Full Support
    - All Tesla products, starting with the Fermi architecture
    - All Quadro products, starting with the Fermi architecture
    - All GRID products, starting with the Kepler architecture
    - GeForce Titan products, starting with the Kepler architecture
- Limited Support
    - All Geforce products, starting with the Fermi architecture


## CLI
```
nvidia-smi [OPTION1 [ARG1]] [OPTION2 [ARG2]] ...
```

LIST OPTIONS:

* `-L,   --list-gpus`
    * Display a list of GPUs connected to the system.

SUMMARY OPTIONS:

* `<no arguments>`
    * Show a summary of GPUs connected to the system.
* `-i,   --id=`
    * Target a specific GPU.
* `-f,   --filename=`
    * Log to a specified file, rather than to stdout.
* `-l,   --loop=`
    * Probe until Ctrl+C at specified second interval.

QUERY OPTIONS:

* `-q,   --query`
    * Display GPU or Unit info.
* `-u,   --unit`
* Show unit, rather than GPU, attributes.
* `-i,   --id=`
    * Target a specific GPU or Unit.
* `-f,   --filename=`
    * Log to a specified file, rather than to stdout.
* `-x,   --xml-format`
    * Produce XML output.
    * `--dtd`
        * When showing xml output, embed DTD.
* `-d,   --display=`
    * Display only selected information:
        * MEMORY
        * UTILIZATION
        * ECC,
        * TEMPERATURE,
        * POWER,
        * CLOCK,
        * COMPUTE,
        * PIDS,
        * PERFORMANCE,
        * SUPPORTED_CLOCKS,
        * PAGE_RETIREMENT,
        * ACCOUNTING,
        * ENCODER STATS
    * Flags can be combined with comma e.g. ECC,POWER.
    * Sampling data with max/min/avg is also returned for POWER, UTILIZATION and CLOCK display types.
    * Doesn't work with `-u` or `-x` flags.
* `-l,   --loop=` 
    * Probe until Ctrl+C at specified second interval.
* `-lms, --loop-ms=`
    * Probe until Ctrl+C at specified millisecond interval.

SELECTIVE QUERY OPTIONS:

Allows the caller to pass an explicit list of properties to query.

[one of]

* `--query-gpu=`
    * Information about GPU.
    * Call `--help-query-gpu` for more info.
* `--query-supported-clocks=`
    * List of supported clocks.
    * Call --help-query-supported-clocks for more info.
* `--query-compute-apps=`
    * List of currently active compute processes.
    * Call --help-query-compute-apps for more info.
* `--query-accounted-apps=`
    * List of accounted compute processes.
    * Call --help-query-accounted-apps for more info.
* `--query-retired-pages=`
    * List of device memory pages that have been retired.
    * Call --help-query-retired-pages for more info.

[mandatory]

* `--format=`
    * Comma separated list of format options:
        * csv - comma separated values (MANDATORY)
        * noheader - skip the first line with column headers
        * nounits - don't print units for numerical values

[plus any of]

* `-i,   --id=`
    * Target a specific GPU or Unit.
* `-f,   --filename=`
    * Log to a specified file, rather than to stdout.
* `-l,   --loop=`
    * Probe until Ctrl+C at specified second interval.
* `-lms, --loop-ms=`
    * Probe until Ctrl+C at specified millisecond interval.

DEVICE MODIFICATION OPTIONS:

[any one of]

* `-pm,  --persistence-mode=`
    * Set persistence mode: 0/DISABLED, 1/ENABLED
* `-e,   --ecc-config=`
    * Toggle ECC support: 0/DISABLED, 1/ENABLED
* `-p,   --reset-ecc-errors=`
    * Reset ECC error counts: 0/VOLATILE, 1/AGGREGATE
* `-c,   --compute-mode=`
    * Set MODE for compute applications:
        * 0/DEFAULT,
        * 1/EXCLUSIVE_PROCESS,
        * 2/PROHIBITED
* `--gom=`
    * Set GPU Operation Mode:
        * 0/ALL_ON,
        * 1/COMPUTE,
        * 2/LOW_DP
* `-r    --gpu-reset`
    * Trigger reset of the GPU.
                            Can be used to reset the GPU HW state in situations
                            that would otherwise require a machine reboot.
                            Typically useful if a double bit ECC error has
                            occurred.
                            Reset operations are not guarenteed to work in
                            all cases and should be used with caution.
-vm   --virt-mode=          Switch GPU Virtualization Mode:
                            Sets GPU virtualization mode to 3/VGPU or 4/VSGA
                            Virtualization mode of a GPU can only be set when
                            it is running on a hypervisor.
-ac   --applications-clocks= Specifies <memory,graphics> clocks as a
                                pair (e.g. 2000,800) that defines GPU's
                                speed in MHz while running applications on a GPU.
-rac  --reset-applications-clocks
                            Resets the applications clocks to the default values.
-acp  --applications-clocks-permission=
                            Toggles permission requirements for -ac and -rac commands:
                            0/UNRESTRICTED, 1/RESTRICTED
-pl   --power-limit=        Specifies maximum power management limit in watts.
-am   --accounting-mode=    Enable or disable Accounting Mode: 0/DISABLED, 1/ENABLED
-caa  --clear-accounted-apps
                            Clears all the accounted PIDs in the buffer.
      --auto-boost-default= Set the default auto boost policy to 0/DISABLED
                            or 1/ENABLED, enforcing the change only after the
                            last boost client has exited.
      --auto-boost-permission=
                            Allow non-admin/root control over auto boost mode:
                            0/UNRESTRICTED, 1/RESTRICTED
[plus optional]

-i,   --id=                 Target a specific GPU.

UNIT MODIFICATION OPTIONS:

-t,   --toggle-led=         Set Unit LED state: 0/GREEN, 1/AMBER

[plus optional]

-i,   --id=                 Target a specific Unit.

SHOW DTD OPTIONS:

      --dtd                 Print device DTD and exit.

 [plus optional]

-f,   --filename=           Log to a specified file, rather than to stdout.
-u,   --unit                Show unit, rather than device, DTD.

--debug=                    Log encrypted debug information to a specified file. 

STATISTICS: (EXPERIMENTAL)
stats                       Displays device statistics. "nvidia-smi stats -h" for more information.

Device Monitoring:
dmon                        Displays device stats in scrolling format.
                            "nvidia-smi dmon -h" for more information.

daemon                      Runs in background and monitor devices as a daemon process.
                            This is an experimental feature. Not supported on Windows baremetal
                            "nvidia-smi daemon -h" for more information.

replay                      Used to replay/extract the persistent stats generated by daemon.
                            This is an experimental feature.
                            "nvidia-smi replay -h" for more information.

Process Monitoring:
pmon                        Displays process stats in scrolling format.
                            "nvidia-smi pmon -h" for more information.

TOPOLOGY:
topo                        Displays device/system topology. "nvidia-smi topo -h" for more information.

DRAIN STATES:
drain                       Displays/modifies GPU drain states for power idling. "nvidia-smi drain -h" for more information.

NVLINK:
nvlink                      Displays device nvlink information. "nvidia-smi nvlink -h" for more information.

CLOCKS:
clocks                      Control and query clock information. "nvidia-smi clocks -h" for more information.

ENCODER SESSIONS:
encodersessions             Displays device encoder sessions information. "nvidia-smi encodersessions -h" for more information.

GRID vGPU:
vgpu                        Displays vGPU information. "nvidia-smi vgpu -h" for more information.

## Usage

## Reference
