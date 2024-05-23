# DogBot

DogBot is a Python project focused on the kinematics of a quadruped robot. The project includes scripts for simulating and plotting the robot's movements using matplotlib.

## Features

- **DH Parameters**: Define the Denavit-Hartenberg parameters for the robot.
- **Leg Inverse Kinematics**: Compute the leg positions for various movements.
- **Movement Patterns**: Includes functions for hopping, pushups, and sit-stand transitions.
- **Visualization**: Plot and simulate the robot's movements using matplotlib.

## Samples

### Visualization of the leg and the DH
![WhatsApp Image 2023-04-27 at 9 24 50 PM](https://user-images.githubusercontent.com/91419527/235078426-427c8d09-09dc-4883-8e00-3d5f4f3cbde9.jpeg)
![WhatsApp Image 2023-04-27 at 9 44 24 PM](https://user-images.githubusercontent.com/91419527/235078165-eddc8bd8-7498-4aaf-bf28-6dd88f0e5d9f.jpeg)

### Static iKin
![image](https://github.com/iCaran/DogBot/assets/91419527/8ed88934-91d3-4c69-ba76-9a4cdc1e0e6b)

### Vector plotting of sitting position
![image](https://user-images.githubusercontent.com/95967684/223419527-11eb0c7e-218c-4c86-8094-8bd8c16da14b.png)

### Translation in 3d space
![translation](https://user-images.githubusercontent.com/95967684/226155969-355b5525-358d-42bc-827a-e51cde32e40e.gif)

### Controlling the limbs manually with set range of possible angles, for demonstration
![fixedcode](https://user-images.githubusercontent.com/91419527/226095731-e9eebcb7-80e2-46f0-9fdd-838f3e7ecbb8.gif)

### PushUp
![output](https://user-images.githubusercontent.com/91419527/227710429-8c3c6d34-0380-4d9e-b374-dae0bd7b4e6b.gif)

### End Effector trajectory, for hopping
![image](https://user-images.githubusercontent.com/91419527/232205572-bc9e7013-b7e2-4653-998c-c29b290ea3c5.png)

### Hopping (by calculating co-ordinates of individual End-Effector positions in a set trajectory
![ani](https://user-images.githubusercontent.com/91419527/232347018-cc7f32a2-8e7a-4f5c-ae35-48c3517fb823.gif)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/iCaran/DogBot.git
   ```
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the main scripts to see the different movement patterns and kinematics simulations:
```bash
python main.py
```

## License

This project is licensed under the UnLicense.

---

Feel free to modify it according to your needs!
