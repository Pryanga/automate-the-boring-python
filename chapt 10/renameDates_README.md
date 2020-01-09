# Rename Dates
## Change the date formats in the filename

### Learning points:
1. grouping in regex comes handy when needed to rearrange the components of the pattern

        re.sub
        
2. os.path.abs takes in the path and by default the current workdir and merge them into something that looks like a path but **not necessary that the path exists**.
    
    os.path.relpath has similar function