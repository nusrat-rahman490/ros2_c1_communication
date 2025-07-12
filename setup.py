from setuptools import setup

package_name = 'basic_comm'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Nusrat Rahman',
    maintainer_email='rahmannusrat490@gmail.com',
    description='Simple ROS2 pub-sub project',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = basic_comm.talker:start_node',
            'listener = basic_comm.listener:start_receiver',
        ],
    },
)

