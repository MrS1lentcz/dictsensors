## Dictsensors

Minimalistic python library which provides data from all sensors via python dict. This library is fully test covered.
It's based on libsensors.so(.x) bindings library from lm-sensors project using ctypes. 
It supports all live versions of python interpreter, including pypy and cython.

### Motivation

None of current python-sensors libraries is maintained, supports python3 language or is test covered.
Motivation was to create one library with very simple usage based on python dict output for maximum comfort and usability.

### Requirements
- libsensors.so(.x) from lm-sensors version 3.x (API 4)
- One of the following interpreters:
	- Python 2.6+ (tested on 2.6.9, 2.7.12) 
	- Python 3.4+ (tested on 3.4.5, 3.5.2, 3.6-dev)
	- Pypy (tested on pypy-5.4.1, pypy2-5.4.1, pypy3-2.4.0)

### Installation

You sure have installed lm-sensors and pip, but just in case:

```
#deb
sudo apt-get install lm-sensors python-pip

#rpm
sudo yum install lm-sensors python-pip
```

Install dictsensors itself via pip within active virtualenv
```
pip install dictsensors
```

### Usage

To be able to collect data from various sensors, a SensorReader class declaration is required.
SensorsReader instance can be declared with or without a "lib_path" argument. In the second case (default) it autodetects libsensors.so automatically. You can however use your own version of the library.

```
from sensors import SensorsReader
reader = SensorsReader()
print(reader.get_data())

reader = SensorsReader(lib_path='/anywhere/libsensors.so.4')
print(reader.get_data())

# Output is shown on the bottom of the documentation
```

### CPU temperature

There is a native support for getting cpu temperature as float number (all values are float numbers).
The main coretemp and acpitz sensor drivers are supported but you can choose arbitrary one by prefix name.

```
# Basic call
from sensors import SensorsReader
reader = SensorsReader()
print(reader.get_cpu_temp())
>>> 56.0

# Call with modified source data
reader = SensorsReader()
data = reader.get_data()
data.update(coretemp=data['unsupported_cpu_sensor'])
print(reader.get_cpu_temp(data))
>>> 45.2

# Chosen custom unsupported sensor
reader = SensorsReader()
print(reader.get_cpu_temp(sensor='unsupported_sensor'))
>>> 29.0
```
 
 
### get_data() output example

```
{
	'acpitz': {
		'features': {
			'temp1': {
				'number': 0,
				'padding1': 0,
				'name': 'temp1',
				'sub_features': {
					'temp1_input': {
						'flags': 5,
						'value': 54.0,
						'number': 0,
						'mapping': 0,
						'name': 'temp1_input',
						'type': 512
					},
					'temp1_crit': {
						'flags': 5,
						'value': 103.0,
						'number': 1,
						'mapping': 0,
						'name': 'temp1_crit',
						'type': 516
					}
				},
				'type': 2,
				'first_subfeature': 0
			}
		},
		'path': '/sys/class/hwmon/hwmon0',
		'addr': 0,
		'prefix': 'acpitz',
		'sensors_bus_id': {
			'type': 4,
			'nr': 0
		}
	},
	'asus': {
		'features': {
			'temp1': {
				'number': 0,
				'padding1': 0,
				'name': 'temp1',
				'sub_features': {
					'temp1_input': {
						'flags': 5,
						'value': 54.0,
						'number': 0,
						'mapping': 0,
						'name': 'temp1_input',
						'type': 512
					}
				},
				'type': 2,
				'first_subfeature': 0
			}
		},
		'path': '/sys/class/hwmon/hwmon2',
		'addr': 0,
		'prefix': 'asus',
		'sensors_bus_id': {
			'type': 1,
			'nr': 0
		}
	},
	'coretemp': {
		'features': {
			'temp1': {
				'number': 0,
				'padding1': 0,
				'name': 'temp1',
				'sub_features': {
					'temp1_input': {
						'flags': 5,
						'value': 54.0,
						'number': 0,
						'mapping': 0,
						'name': 'temp1_input',
						'type': 512
					},
					'temp1_max': {
						'flags': 5,
						'value': 100.0,
						'number': 1,
						'mapping': 0,
						'name': 'temp1_max',
						'type': 513
					},
					'temp1_crit_alarm': {
						'flags': 1,
						'value': 0.0,
						'number': 3,
						'mapping': 0,
						'name': 'temp1_crit_alarm',
						'type': 643
					},
					'temp1_crit': {
						'flags': 5,
						'value': 100.0,
						'number': 2,
						'mapping': 0,
						'name': 'temp1_crit',
						'type': 516
					}
				},
				'type': 2,
				'first_subfeature': 0
			},
			'temp3': {
				'number': 2,
				'padding1': 0,
				'name': 'temp3',
				'sub_features': {
					'temp3_input': {
						'flags': 5,
						'value': 52.0,
						'number': 8,
						'mapping': 2,
						'name': 'temp3_input',
						'type': 512
					},
					'temp3_crit_alarm': {
						'flags': 1,
						'value': 0.0,
						'number': 11,
						'mapping': 2,
						'name': 'temp3_crit_alarm',
						'type': 643
					},
					'temp3_crit': {
						'flags': 5,
						'value': 100.0,
						'number': 10,
						'mapping': 2,
						'name': 'temp3_crit',
						'type': 516
					},
					'temp3_max': {
						'flags': 5,
						'value': 100.0,
						'number': 9,
						'mapping': 2,
						'name': 'temp3_max',
						'type': 513
					}
				},
				'type': 2,
				'first_subfeature': 8
			},
			'temp2': {
				'number': 1,
				'padding1': 0,
				'name': 'temp2',
				'sub_features': {
					'temp2_max': {
						'flags': 5,
						'value': 100.0,
						'number': 5,
						'mapping': 1,
						'name': 'temp2_max',
						'type': 513
					},
					'temp2_crit_alarm': {
						'flags': 1,
						'value': 0.0,
						'number': 7,
						'mapping': 1,
						'name': 'temp2_crit_alarm',
						'type': 643
					},
					'temp2_crit': {
						'flags': 5,
						'value': 100.0,
						'number': 6,
						'mapping': 1,
						'name': 'temp2_crit',
						'type': 516
					},
					'temp2_input': {
						'flags': 5,
						'value': 53.0,
						'number': 4,
						'mapping': 1,
						'name': 'temp2_input',
						'type': 512
					}
				},
				'type': 2,
				'first_subfeature': 4
			}
		},
		'path': '/sys/class/hwmon/hwmon1',
		'addr': 0,
		'prefix': 'coretemp',
		'sensors_bus_id': {
			'type': 1,
			'nr': 0
		}
	}
}
```

### Licence
MIT License Copyright (c) 2017  Jiri Dubansky

### Contributors
- [MrS1lentcz](https://github.com/MrS1lentcz) (author)
- [Don Mums](https://github.com/don-mums)
