{
  'targets': [
    {
      'target_name': 'libsodium',
      'dependencies': [
        'deps/libsodium.gyp:libsodium',
      ],
      'include_dirs' : [
        "<!(node -e \"require('nan')\")",
        'deps/libsodium',
      ],
      'sources': [
        'binding.cc',
      ],
   }
  ]
}
