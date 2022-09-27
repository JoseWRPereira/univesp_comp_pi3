import React from 'react'
import Typography from '@mui/material/Typography';
import Card from '@mui/material/Card';
import Box from '@mui/material/Box';
import Avatar from '@mui/material/Avatar';
import Stack from '@mui/material/Stack';
import Divider from '@mui/material/Divider';

export default function FirstPage() {

    return (
      <div>
        <Card>
          <Box sx={{ p: 2, display: 'flex' }}>
            <Avatar variant="rounded" src="people.jpeg" />
            <Stack spacing={0.5}>
              <Typography fontWeight={700}>Nome Do Familiar</Typography>
              <Typography variant="body2" color="text.secondary">
              </Typography>
            </Stack>
          </Box>
          <Divider />
          <Stack
            direction="row"
            alignItems="center"
            justifyContent="space-between"
            sx={{ px: 2, py: 1, bgcolor: 'background.default' }}
          >
            <h3>Nome do Filho</h3>
          </Stack>
        </Card>
      </div>
    )
  }
