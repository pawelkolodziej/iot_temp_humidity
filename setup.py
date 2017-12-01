from setuptools import setup

setup(
    name='iot_temp_humidity',
    version='0.1',
    packages=['iot_temp_humidity'],
    url='https://github.com/pawelkolodziej/iot_temp_humidity',
    license='MIT',
    author='PawelK',
    author_email='pakolodziej@gmail.com',
    description='RaspberryPi - get temp and humidity from sensor',
    install_requires=['schedule','adafruit_python_dht','PyFCM']
)
