import pymysql

'CREATE DATABASE [AffinityDB]'

# Create database AffinityDB and specify physical file locations, initial physical file sizes, and autogrowth increments, change owner to sa, and set compatibility level to lower version CREATE DATABASE [AffinityDB] 
ON (NAME = N'AffinityDB', FILENAME = , SIZE = 1024MB, FILEGROWTH = 256MB)
LOG ON (NAME = N'AffinityDB', FILENAME = , SIZE = 512MB, FILEGROWTH = 125MB)
GO

# Change owner to sa
'ALTER AUTHORIZATION ON DATABASE::[AffinityDB] TO [sa]'
GO

# Set recovery model to simple 
'ALTER DATABASE [AffinityDB] SET RECOVERY SIMPLE'
GO

# Change compatibility level
'ALTER DATABASE [AffinityDB] SET COMPATIBILITY_LEVEL = 130'
GO
# Set to multi-user
'ALTER DATABASE [AffinityDB] SET MULTI_USER'
GO

# Set permissions
'ALTER DATABASE [AffinityDB] SET READ_WRITE'
GO

# Global cursor
'ALTER DATABASE [AffinityDB] SET CURSOR_DEFAULT GLOBAL'
GO