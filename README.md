# SolarSystemPlanner

SolarSystemPlanner is a Python library that helps you to realize your photovoltaic system and become independent of carbon energy.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install SolarSystemPlanner.

```bash
pip install solarsystemplanner
```

## Usage

```python
import solarsystemplanner as ssp

# returns '9' as kw system size
yearly_consumption = 1379 # number of power units [in kwH] 
ssp.estimate_size(yearly_consumption)
```

The best is to follow the flow in the [Juypter notebook](notebook.ipynb).

## Resources
- [Solar Power for Beginners](https://www.amazon.de/-/en/Lawrence-Lawson/dp/B08MTZ5HH4)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)