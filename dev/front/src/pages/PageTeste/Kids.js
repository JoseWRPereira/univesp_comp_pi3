import * as React from 'react';
import { DataGrid, GridRowsProp, GridColDef } from '@mui/x-data-grid';

const rows: GridRowsProp = [
  { id: 1, col1: '2022-10-10', col2: 'Sim', col3: 'Sim' },
  { id: 2, col1: '2022-10-11', col2: 'Sim', col3: 'Sim' },
  { id: 3, col1: '2022-10-12', col2: 'Nao', col3: 'Sim' },
];

const columns: GridColDef[] = [
  { field: 'col1', headerName: 'Data', width: 150 },
  { field: 'col2', headerName: 'Café', width: 150 },
  { field: 'col3', headerName: 'Almoço', width: 150 },
];


export default function Kids() {
  return (
    <div style={{ height: 300, width: '100%' }}>
      <DataGrid rows={rows} columns={columns} hideFooterPagination hideFooterSelectedRowCount />
    </div>
  )
}
