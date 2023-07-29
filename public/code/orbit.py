import numpy as np
import matplotlib.pyplot as plt
import imageio
import os

def simulate_orbit(G, m1, m2, r1_initial, r2_initial, v1_initial, v2_initial, dt, steps):
    # Initialize position and velocity arrays for both bodies
    r1 = np.zeros((steps+1, 2))
    r2 = np.zeros((steps+1, 2))
    v1 = np.zeros((steps+1, 2))
    v2 = np.zeros((steps+1, 2))
    
    r1[0] = r1_initial
    r2[0] = r2_initial
    v1[0] = v1_initial
    v2[0] = v2_initial
    
    # Calculate path
    for i in range(steps):
        r = r2[i] - r1[i]  # relative position vector
        F = -G * m1 * m2 / np.linalg.norm(r)**3 * r  # gravitational force
        a1 = F / m1  # acceleration of body 1
        a2 = -F / m2  # acceleration of body 2 (equal and opposite)
        v1[i+1] = v1[i] + a1*dt  # update velocity of body 1
        v2[i+1] = v2[i] + a2*dt  # update velocity of body 2
        r1[i+1] = r1[i] + v1[i+1]*dt  # update position of body 1
        r2[i+1] = r2[i] + v2[i+1]*dt  # update position of body 2

    return r1, r2, v1, v2

def create_frames(r1, r2, filename, frame_interval):
    frames_path = "public/images/frames/orbits/"
    os.makedirs(frames_path, exist_ok=True)
    filenames = []

    for i in range(0, len(r1), frame_interval):
        plt.figure()
        plt.plot(r1[i, 0], r1[i, 1], 'ro')  # plot E
        plt.plot(r2[i, 0], r2[i, 1], 'bo')  # plot P
        plt.xlim(-1.5*np.amax(np.abs(r2)), 1.5*np.amax(np.abs(r2)))
        plt.ylim(-1.5*np.amax(np.abs(r2)), 1.5*np.amax(np.abs(r2)))
        temp_filename = f"{frames_path}frame_{i:04d}.png"
        plt.savefig(temp_filename)
        filenames.append(temp_filename)
        plt.close()

    return filenames

def simulate_and_create_gif(G, m1, m2, r1_initial, r2_initial, v1_initial, v2_initial, dt, steps, gif_filename, frame_interval):
    r1, r2, v1, v2 = simulate_orbit(G, m1, m2, r1_initial, r2_initial, v1_initial, v2_initial, dt, steps)
    filenames = create_frames(r1, r2, gif_filename, frame_interval)
    gif_filename = create_gif(filenames, gif_filename)
    return gif_filename

def create_gif(filenames, gif_filename):
    with imageio.get_writer(gif_filename, mode='I') as writer:
        for filename in filenames:
            image = imageio.imread(filename)
            writer.append_data(image)
    return gif_filename

G = 1  # gravitational constant
m1 = 1  # mass of E
m2 = 0.001  # mass of P
r1_initial = np.array([-0.5, 0])  # initial position of E
r2_initial = np.array([0.5, 0])  # initial position of P
v1_initial = np.array([0, -0.005])  # initial velocity of E
v2_initial = np.array([0, 0.005])  # initial velocity of P
dt = 0.01  # time step
steps = 1000  # number of steps
frame_interval = 33  # generate a frame every 33 steps
gif_filename = "public/images/orbit.gif"  # output filename

simulate_and_create_gif(G, m1, m2, r1_initial, r2_initial, v1_initial, v2_initial, dt, steps, gif_filename, frame_interval)
