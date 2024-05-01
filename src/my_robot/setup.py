from setuptools import setup

package_name = 'my_robot'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Votre Nom',
    maintainer_email='votre.email@example.com',
    description='Package pour le contrôle de mouvement de robot',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'movement_controller = my_robot.movement_controller:main',
        ],
    },
)
