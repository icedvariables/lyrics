import re

RE_BLOCK = re.compile(r"\[(.+):\]") # "[Chorus:]", "[Verse 1:]"
RE_MULTIPLY = re.compile(r"\[([0-9]+)x\]") # "[x4]", "[x12]"

class Lyrics:
    def __init__(self, text):
        self.blocks = {"main":[]}
        currentBlock = "main"
        multiplyNextLine = 0

        for line in text.split("\n"):
            line = line.strip()

            if not(line):
                currentBlock = "main"
                continue

            match = RE_BLOCK.match(line)
            if(match):
                block = match.group(1)
                print "Found block:", block

                # If a block witrh the same name already exists, rename this block to "name_number"
                # eg. If "chorus" is already defined and it is found again, then the new block would become "chorus_0", then the next would be "chorus_1" and so on
                i = 0
                original = block
                while(block in self.blocks.keys()):
                    block = original + "_" + str(i)
                    i += 1

                if(i > 0):
                    print "Block named changed as a block with the same name already exists:", block

                self.blocks[block] = []
                currentBlock = block

                continue

            match = RE_MULTIPLY.match(line)
            if(match):
                amount = int(match.group(1))
                print "Found multiply:", amount

                multiplyNextLine = amount

                continue

            if(multiplyNextLine > 0):
                self.blocks[currentBlock].extend([line] * multiplyNextLine)
                multiplyNextLine = 0
            else:
                self.blocks[currentBlock].append(line)
