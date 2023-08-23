import matplotlib.pyplot as plt

def plot_eye_data(time_data, ear_data, blink_data, file_name):
  fig, axes = plt.subplots(nrows=2, figsize=(20, 12))

  # First subplot
  axes[0].plot(time_data, ear_data)
  axes[0].set_title("Eye Data")
  axes[0].set_xlabel("Time Elapsed (s)")
  axes[0].set_ylabel("EAR")
  
  # Second subplot
  axes[1].set_title("Blink Data")
  axes[1].plot(time_data, blink_data)
  axes[1].set_xlabel("Time Elapsed (s)")
  axes[1].set_ylabel("Blink (Y/N)")

  # Adjust spacing between subplots
  plt.tight_layout(pad=2.0)

  # Save the figure
  plt.savefig(f"{file_name}_eyedata.png", bbox_inches='tight')
  plt.clf()


def plot_mouth_data(time_data, mar_data, yawn_data, file_name):
  fig, axes = plt.subplots(nrows=2, figsize=(20, 12))

  # First subplot
  axes[0].plot(time_data, mar_data)
  axes[0].set_title("Mouth Data")
  axes[0].set_xlabel("Time Elapsed (s)")
  axes[0].set_ylabel("MAR")

  # Second subplot
  axes[1].set_title("Yawn Data")
  axes[1].plot(time_data, yawn_data)
  axes[1].set_xlabel("Time Elapsed (s)")
  axes[1].set_ylabel("Yawn (Y/N)")

  # Adjust spacing between subplots
  plt.tight_layout(pad=2.0)

  # Save the figure
  plt.savefig(f"{file_name}_mouthdata.png", bbox_inches='tight')
  plt.clf()