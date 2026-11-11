import torch

print("PyTorch version:", torch.__version__)
print("PyTorch CUDA runtime:", torch.version.cuda)
print("CUDA available:", torch.cuda.is_available())

if torch.cuda.is_available():
    print("GPU name:", torch.cuda.get_device_name(0))

    x = torch.tensor([1, 2, 3], device="cuda")

    print("Tensor:", x)
    print("Tensor location:", x.device)
else:
    print("GPU is not available.")