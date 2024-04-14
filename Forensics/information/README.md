# information

Tags: picoCTF 2021, Forensics

| Author | Point    |
| ------ | -------- |
| SUSIE | 10 points |

## Description

Files can always be changed in a secret way. Can you find the flag?

## Hints

1. Look at the details of the file
2. Make sure to submit the flag as picoCTF{XXXXX}

## Solve

I used exiftool online to view exif.

https://exif.tools/

Lisence is strange.


| Name                           | Value                                         |
|--------------------------------|-----------------------------------------------|
| ExifTool Version Number        | 12.25                                         |
| File Name                      | phpfvJJK8                                     |
| Directory                      | /tmp                                          |
| File Size                      | 858 KiB                                       |
| File Modification Date/Time    | 2024:04:14 23:26:30+00:00                     |
| File Access Date/Time          | 2024:04:14 23:26:29+00:00                     |
| File Inode Change Date/Time    | 2024:04:14 23:26:30+00:00                     |
| File Permissions               | -rw-------                                    |
| File Type                      | JPEG                                          |
| File Type Extension            | jpg                                           |
| MIME Type                      | image/jpeg                                    |
| JFIF Version                   | 1.02                                          |
| Resolution Unit                | None                                          |
| X Resolution                   | 1                                             |
| Y Resolution                   | 1                                             |
| Current IPTC Digest            | 7a78f3d9cfb1ce42ab5a3aa30573d617               |
| Copyright Notice               | PicoCTF                                       |
| Application Record Version     | 4                                             |
| XMP Toolkit                    | Image::ExifTool 10.80                         |
| License                        | cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9   |
| Rights                         | PicoCTF                                       |
| Image Width                    | 2560                                          |
| Image Height                   | 1598                                          |
| Encoding Process               | Baseline DCT, Huffman coding                  |
| Bits Per Sample                | 8                                             |
| Color Components               | 3                                             |
| Y Cb Cr Sub Sampling           | YCbCr4:2:0 (2 2)                              |
| Image Size                     | 2560x1598                                     |
| Megapixels                     | 4.1                                           |

```bash
$ echo cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9 | base64 -d
picoCTF{the_m3tadata_1s_********}
```

## Flag

```
picoCTF{the_m3tadata_1s_********}
```