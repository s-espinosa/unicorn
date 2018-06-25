from letters import letters

class MessageMovie:
    def __init__(self, message):
        self.refresh_rate = 0.025
        self.finished = False
        self.rotation = 0
        self.frame    = 0
        self.message  = message

    def step(self):
        pixels = []
        next_frame = [0] * 256
        for index, item in enumerate(self.heart):
            x = index % 16
            y = ((index - x) / 16) % 16

            if item == 0:
                r = 0.0
                b = 0.0
            else:
                r = 255.0
                b = 255.0
            pixels.append({"x": x, "y": y, "r": r, "g": 0, "b": b})
            if index % 16 == 15:
                next_position = index - 15
            else:
                next_position = index + 1
            next_frame[next_position] = item

        self.frame = self.frame + 1
        self.heart = next_frame

        return pixels

    def generate_encrypted_message(self):
        """docstring for generate_encrypted_message"""
        individual_letters = self.split_message
        encrypted_letters  = self.message_arrays(individual_letters)
        encrypted_message  = self.join(encrypted_letters)

    def split_message(self):
        """docstring for letters"""
        self.message.split("")

    def message_arrays(self, letters_in_message):
        """docstring for message_arrays"""
        encrypted_letters = []
        for letter in letters_in_message:
            encrypted_letters.append(letters[letter])
        return encrypted_letters

    def join(self, encrypted_letters):
        """docstring for join"""
        rows = [[]] * 16
