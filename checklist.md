# PDF Cropping Implementation Checklist

## Core PDF Processing
- [ ] Create main cropping function structure
  - [ ] Read input PDF
  - [ ] Process specified page ranges
  - [ ] Calculate mediabox dimensions for splits
  - [ ] Create new pages from splits
  - [ ] Write output PDF

## Command Line Interface
- [ ] Add new `--crop-half` argument to existing CLI
- [ ] Update argument parsing for page ranges
- [ ] Connect CLI to PDF processing function
> It will only do cropping by half, no matter if the pdf page needs it or not (user decides)

## Error Handling
- [ ] Validate input PDF exists and is readable
- [ ] Verify page ranges are within PDF bounds
- [ ] Handle PDF writing permissions
- [ ] Add appropriate error messages

## Future Considerations
- [ ] Plan separation of PDF logic from CLI
- [ ] Document mediabox calculations for maintainability
- [ ] Prepare structure for future GUI integration

## Testing
- [ ] Create sample PDF for testing
- [ ] Test with various page ranges
- [ ] Test with different PDF sizes/orientations
- [ ] Add unit tests for new functionality

# Things to do
- [ ] Refactor and create arguments and pass them into the Cmdline class
- [ ] Create a new command where it cropts by half and creates a new
          - [ ] Using the media box for cropping i would do the following changes
> pdf-tool -f file.pdf --crop-half 20-40 89-90

